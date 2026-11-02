# xishanp/Linuxhub

⭐ 59 · C · GPL-3.0 · 推送 2026-11-01 · [GitHub](https://github.com/xishanp/Linuxhub) · 个人维护 · 中文 README

**在 Android 上运行 Ubuntu 桌面并供本机 Agent 调用的环境**

面向 Android 8.0+ ARM64 设备的 Android 应用：通过 PRoot 部署 Ubuntu 24.04 用户空间与 XFCE 桌面（Termux:X11 显示链路），提供触控操作、中文 locale/Fcitx5 输入法、多会话终端与剪贴板等桌面能力。内置仅监听 127.0.0.1 的本机 Agent REST API（Bearer Token 鉴权），Agent 可调用终端、窗口、截图、鼠标键盘、剪贴板等工具，并经 Shizuku 执行 Android 系统级操作。无需 Root，PRoot 非安全沙箱，APK 从源码用 Gradle 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PRoot 部署 Ubuntu 24.04 + XFCE 桌面，无需 Root
- 本机 Agent REST API（仅监听 127.0.0.1，Bearer Token 鉴权），暴露终端/窗口/输入/截图等结构化工具
- 经 Shizuku 提供 Android shell 身份，支持 APK 安装、系统级输入与文件推拉
- 完整中文桌面链路：zh_CN.UTF-8、Noto CJK、Fcitx5 与 Agent UTF-8 输入

## 适用场景

- 在手机/平板上获得可触控操作的完整 Linux 桌面环境
- 让本机 Agent 通过 REST API 自动操作桌面执行连续任务
- 通过 Agent 调用 Android 系统能力（截图、输入、APK 管理）

## 场景标签

 · 领域:移动/Linux 桌面与 Agent 环境

## 证据(README 行号)

> L3:  把 Android 变成一台完整的 Linux 工作站，也变成 Agent 可以直接操作的本地电脑。
> L29: 它把原本分散的终端、Linux 桌面、图形窗口、鼠标键盘、Android 系统能力和自动化接口整合到同一个应用中。用户可以像使用普通 Linux 电脑一样操作桌面，也可以让可信 Agent 通过本机 REST API 完成连续任务
> L53: LinuxHub 内置仅监听 `127.0.0.1` 的 Agent API。Agent 可以枚举应用和窗口、启动桌面、截图裁切、移动鼠标、输入文字、执行终端命令，并在需要时调用 Shizuku 完成 Android 系统级操作。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `8fac65df0a2c` · [字段定义](../../DATASET.md)*
