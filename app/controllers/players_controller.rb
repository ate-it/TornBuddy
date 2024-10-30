class PlayersController < ApplicationController
  def create
    key = params["player"]["key"]
    print (key)
  end
end
