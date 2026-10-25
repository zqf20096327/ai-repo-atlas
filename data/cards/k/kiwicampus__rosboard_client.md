# kiwicampus/rosboard_client

⭐ 46 · Python · GPL-3.0 · 推送 2026-09-17 · [GitHub](https://github.com/kiwicampus/rosboard_client) · 组织维护

**通过 websocket 从远程机器人选择性串流 ROS 话题的桌面客户端**

配合 kiwicampus 自维护的 rosboard 服务端 fork 使用的客户端库：在远程机器人上运行 rosboard 服务端，本地通过 websocket 订阅选定话题，接收二进制数据解码后交给回调；提供 republisher 将 json 转回 ROS 消息本地再发布，支持图像、LaserScan、PointCloud2、OccupancyGrid 的子采样与压缩还原，并带 GUI 客户端展示消息速率、延迟、RTT 与下载速度。网络模块与 ROS 解耦可独立使用。限制：必须使用其自有 rosboard fork 作为服务端。以 git clone 源码方式安装并用 colcon 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选择性订阅远程 ROS 话题并通过 websocket 串流
- republisher 将 rosboard json 转回 ROS 消息本地发布，处理图像/激光/点云/栅格的压缩与子采样
- GUI 客户端展示消息速率、延迟、RTT、CPU 与下载速度
- 网络模块可脱离 ROS 独立使用自定义回调

## 适用场景

- 在本地用 rviz/rqt/mapviz 可视化远程机器人实时数据
- 蜂窝网络环境下低带宽串流相机等高数据率传感器话题
- 通过 ngrok 隧道在互联网上远程调试机器人

## 场景标签

 · 领域:机器人/ROS 工具

## 证据(README 行号)

> L2: The main objective of this library is to selectively stream ROS topics using websockets from a remote robot to a loc
> L24: This library provides a desktop client that connects to a remote rosboard server and allows to create subscriptions

## 星数曲线

```mermaid
xychart-beta
    title "kiwicampus/rosboard_client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `cc752a961541` · [字段定义](../../DATASET.md)*
