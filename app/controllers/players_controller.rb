class PlayersController < ApplicationController
  def create
    key = params["player"]["key"]
    print (key)
  end

  def new
    # TODO: if player is logged in, redirect to dashboard
    @player = Player.new
  end
end
