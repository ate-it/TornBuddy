class StaticController < ApplicationController
  def index
    # TODO: if player is logged in, redirect to dashboard
  end

  def signin
    # TODO: if player is logged in, redirect to dashboard
    @player = Player.new
  end
end
