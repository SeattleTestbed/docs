package seattle.sensortest;

import java.util.HashMap;
import java.util.Map;
import org.apache.xmlrpc.XmlRpcException;
import org.apache.xmlrpc.XmlRpcRequest;
import org.apache.xmlrpc.server.PropertyHandlerMapping;
import org.apache.xmlrpc.server.RequestProcessorFactoryFactory;
import org.apache.xmlrpc.server.XmlRpcServer;
import org.apache.xmlrpc.server.XmlRpcServerConfigImpl;
import org.apache.xmlrpc.server.RequestProcessorFactoryFactory.RequestProcessorFactory;
import org.apache.xmlrpc.webserver.WebServer;
 
/** A simple implementation of XML-RPC server for apache ws-xmlrpc
 * Version 1.2 - support single instance handler object, but not yet multi-threaded  */
public class SimpleXmlRpcServer
{
	/* ======================================== runtime attr ========================================== */
	private int port;
	private WebServer webServer = null;
	private PropertyHandlerMapping phm = null;
	private SimpleXmlRpcRequestHandlerFactory handler = null;
	private XmlRpcServer xmlRpcServer = null;
 
	/* ======================================== init/destroy ========================================== */ 
	/** Creates an instance of xml rpc server, using :handler as the class that  will handle all request. 
	 * Note that a new instance of :handler will be created at every xml-rpc request.
	 * @param name
	 * @param port
	 * @param handler
	 * @throws Exception */
	public SimpleXmlRpcServer(int port) throws Exception
	{
		this.port = port;
		this.webServer = new WebServer(this.port); 	// bind
		this.xmlRpcServer = this.webServer.getXmlRpcServer();
		this.handler = new SimpleXmlRpcRequestHandlerFactory(); 
		this.phm = new PropertyHandlerMapping();
		this.phm.setRequestProcessorFactoryFactory(this.handler);
	}
 
	/* ======================================== services ========================================== */ 
	/** Adds a handler instance (which CAN be stateful) for each request. Note that
	 * every public method in this object will be callable via xml-rpc client
	 * @param name - handler name
	 * @param requestHandler - handler obj instance
	 * @throws Exception */
	public void addHandler(String name, Object requestHandler) throws Exception
	{
		this.handler.setHandler(name, requestHandler);
		this.phm.addHandler(name, requestHandler.getClass());
	}
 
	/** Start the xml-rpc server forever. In the rare case of fatal exception, the web server will be 
	 * restarted automatically. This is a blocking call (not thread-based). */
	public void serve_forever() throws Exception
	{
		this.xmlRpcServer.setHandlerMapping(phm);
		XmlRpcServerConfigImpl serverConfig = (XmlRpcServerConfigImpl) xmlRpcServer.getConfig();
		serverConfig.setEnabledForExtensions(true);
		this.webServer.start();
	}
 
	/* ====================================== getter/setter ======================================== */ 
	public int getPort() { return port; }
	public void setPort(int port) { this.port = port; }
	public WebServer getWebServer() { return webServer; }
	public void setWebServer(WebServer webServer) { this.webServer = webServer; }
	public PropertyHandlerMapping getPhm() { return phm; }
	public void setPhm(PropertyHandlerMapping phm) { this.phm = phm; }
	public SimpleXmlRpcRequestHandlerFactory getHandler() { return handler; }
	public void setHandler(SimpleXmlRpcRequestHandlerFactory handler) { this.handler = handler; }
	public XmlRpcServer getXmlRpcServer() { return xmlRpcServer; }
	public void setXmlRpcServer(XmlRpcServer xmlRpcServer) { this.xmlRpcServer = xmlRpcServer; } 
 
}

class SimpleXmlRpcRequestHandlerFactory implements RequestProcessorFactoryFactory, RequestProcessorFactory
{
	private Map handlerMap = new HashMap();
	
	public void setHandler(String name, Object handler) { this.handlerMap.put(name, handler); }
	public Object getHandler(String name) { return this.handlerMap.get(name); }
 
	public RequestProcessorFactory getRequestProcessorFactory(Class arg0) throws XmlRpcException { return (RequestProcessorFactory) this; }
	
	public Object getRequestProcessor(XmlRpcRequest request) throws XmlRpcException
	{
		String handlerName = request.getMethodName().substring(0,request.getMethodName().lastIndexOf("."));
		if( !handlerMap.containsKey(handlerName)) throw new XmlRpcException("Unknown handler: "+handlerName);
		return handlerMap.get(handlerName);
	}
}