package com.mock.restserver;

import java.util.concurrent.atomic.AtomicInteger;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;

@Path("/")
public class RestService {

	private static AtomicInteger counter = new AtomicInteger(0);

	@GET
	@Path("resetcounter")
	public void reset() {
		counter = new AtomicInteger(0);
	}

	@GET
	@Path("counter")
	@Produces("text/plain")
	public int counter() {
		return counter.get();
	}

	@POST
	@Path("postform")
	@Produces("text/plain")
	public String postCommand(@QueryParam("content") String content) {
		counter.incrementAndGet();
//		System.out.println(counter + " received=" + content.length());
		return "received (" + counter.get() + ")";
	}

}
