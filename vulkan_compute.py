'''
    A simple python implementation of a vulkan api wrapper by realitix
    located here: https://github.com/realitix/vulkan which is a rewrite of
    the original pyvulkin on github. "pip install vulkan"

    I found the triangle demo often cited as overly complicated so this is
    my attempt to write a more simplistic demo while also learning vulkan
    and the API wrapper.
'''
__author__ = "Trixanna"
__date__ = "$Jan 22, 2018 09:50:13 PM$"

import vulkan as vk

def init_instance():
    ''' Most things set to default values courtesy of the vulkan wrapper to the API '''

    application_info = vk.VkApplicationInfo(
        sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO
    )

    instance_create_info = vk.VkInstanceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
        pApplicationInfo=application_info,
        enabledLayerCount=0,
        enabledExtensionCount=0
    )

    #allocation = vk.vkAllocateMemory()
    instance = vk.vkCreateInstance(
        instance_create_info,
        pAllocator=None
    )

    if vk.VK_SUCCESS == 0:
        print("debug: instance creation success")
    else:
        print("Failed to create instance. Error: {}".format(vk.VK_SUCCESS))
    
    return instance

def init_device(instance):
    ''' Enumerate and initialize a device '''
    print("Incomplete")
    gpu_count = 0
    gpu_count = vk.vkEnumeratePhysicalDevices(instance,)
    print("Enumerated Device: {}".format(gpu_count[0]))
    properties = vk.vkGetPhysicalDeviceFormatProperties(
        gpu_count[0],
        vk.VK_FORMAT_B8G8R8_UINT,
    )
    #features = vk.vkGetPhysicalDeviceFeatures(gpu)

    queue_family = vk.vkGetPhysicalDeviceQueueFamilyProperties(gpu_count[0])
    print("Queue families: {}".format(queue_family[0]))
    device_queue_info = vk.VkDeviceQueueCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO,
        queueFamilyIndex=1,
        queueCount=1,
        pQueuePriorities=1.0
    )

    device_info = vk.VkDeviceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
        queueCreateInfoCount=1,
        pQueueCreateInfos=device_queue_info,
        enabledExtensionCount=0,
        ppEnabledLayerNames=None,
        ppEnabledExtensionNames=None,
        pEnabledFeatures=None,
        enabledLayerCount=0
    )
    vk.vkCreateDevice(
        gpu_count[0],
        pCreateInfo = 0,
        pAllocator = 0
    )

def main():
    ''' Temp main runner for development '''
    instance = init_instance()
    init_device(instance)

if __name__ == '__main__':
    main()
