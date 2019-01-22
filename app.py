# -*- coding: utf-8 -*-

"""app.py: Simple demo showing how get arguments from the URL.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/users/<int:id>/edit", methods=["GET"])
def route_edit_user(id):
    msg = "You want to edit the user with ID: {} | Arg type: {}".format(id, type(id))
    print(msg)

    return jsonify(msg)


@app.route("/order/from/<string:order_from>/to/<string:order_to>", methods=["GET"])
def route_get_orders_by_location(order_from, order_to):
    msg = "You want to see the orders from {} to {}... | Arg type: order_from: {} | order_to: {}".format(
        order_from.upper(), order_to.upper(), type(order_from), type(order_to))
    print(msg)

    return jsonify(msg)


@app.route("/double/<float:double_this>", methods=["GET"])
def route_double(double_this):
    msg = "You want double {}... which is {}... | Arg type: {}".format(double_this, double_this*2, type(double_this))
    print(msg)

    return jsonify(msg)


@app.route("/querystring", methods=["GET"])
def route_query_string():
    msg = "You passed {} args using query string. Your args: {}".format(len(request.args), request.args)
    print(msg)

    return jsonify(msg)


if __name__ == '__main__':
    app.run()
