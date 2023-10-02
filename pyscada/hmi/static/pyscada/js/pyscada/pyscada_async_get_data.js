var async_get_data_url = '/json/async_cache_data/?variables=' + VARIABLE_KEYS + "&variable_properties=" + VARIABLE_PROPERTY_KEYS + "&timestamp_from=" + DATA_FROM_TIMESTAMP
var source = new EventSource(async_get_data_url);
source.addEventListener("message_created", function(evt) {console.log(JSON.parse(evt.data));})
//source.onopen = (e) => {console.log(e);}
//source.onmessage = (e) => {console.log(e);}
source.onerror = (e) => {
  if (source.readyState != 0) {
    console.log("async get data ERROR !")
  }
}



return {"type": "variable", "id": self.variable.id, "timestamp": timestamp, "value": value, "date_saved": await sync_to_async(self.date_saved.timestamp)()}


if(typeof(EventSource) !== "undefined") {
  // Yes! Server-sent events support!
  // Some code.....
} else {
  // Sorry! No server-sent events support..
}


clear();
var cache_received = []
var aget_cache_data_url = '/json/aget_cache_data/?variables=' + VARIABLE_KEYS + "&timestamp_from=0" // + DATA_FROM_TIMESTAMP
var source_cache = new EventSource(aget_cache_data_url);
source_cache.addEventListener("cache_data", function(evt) {
  console.log(JSON.parse(evt.data));
  cache_received.push(JSON.parse(evt.data));
  if (JSON.parse(evt.data).length == 0) {
	  source_cache.close();
  }
})
//source_cache.onopen = (e) => {console.log(e);}
//source_cache.onmessage = (e) => {console.log(e);}
source_cache.onerror = (e) => {
  if (source_cache.readyState != 0) {
    console.log("aget cache data ERROR !");
  }
}
console.log(cache_received);

var aget_last_data_url = '/json/aget_last_data/?variables=' + VARIABLE_KEYS + "&variable_properties=" + VARIABLE_PROPERTY_KEYS + "&timestamp_from=0" // + DATA_FROM_TIMESTAMP
var source_last = new EventSource(aget_last_data_url);
source_last.addEventListener("cache_data", function(evt) {
  console.log(JSON.parse(evt.data));
  if (!JSON.parse(evt.data).length) {
	  source_last.close();
  }
})
//source_cache.onopen = (e) => {console.log(e);}
//source_cache.onmessage = (e) => {console.log(e);}
source_last.onerror = (e) => {
  if (source_last.readyState != 0) {
    console.log("aget last data ERROR !");
  }
}

var aget_new_data_url = '/json/aget_new_data/?variables=' + VARIABLE_KEYS + "&variable_properties=" + VARIABLE_PROPERTY_KEYS + "&timestamp_from=" + DATA_FROM_TIMESTAMP
var source_new = new EventSource(aget_new_data_url);
source_new.addEventListener("new_data", function(evt) {
  console.log(JSON.parse(evt.data));
})
//source_new.onopen = (e) => {console.log(e);}
//source_new.onmessage = (e) => {console.log(e);}
source_new.onerror = (e) => {
  if (source_new.readyState != 0) {
    console.log("aget new data ERROR !");
  }
}

import channels.layers
channel_layer = channels.layers.get_channel_layer()
await channel_layer.send("PyScadaFromDevice", {"text": "test"})
