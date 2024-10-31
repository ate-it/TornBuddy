module ApiHelper
  def api_call(version, section, selections, key)
    case version
    when 2
      base_url = "https://api.torn.com/v2/"
    when 1
      base_url = "https://api.torn.com/"
    end

      call_string = base_url+section="?key="+key
      response = Faraday.get(call_string)

      JSON.parse(response.body)
  end
end
