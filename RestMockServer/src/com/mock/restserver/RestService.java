package com.mock.restserver;

import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;

@Path("/")
public class RestService  {

	@POST
	@Path("postform")
	@Produces("text/plain")
	public String postCommand(@QueryParam("content") String content) {
		System.out.println("received=" + content.length());
		return "received";
	}

}
