# sonnvntu/openviewer-releases

⭐ 24 · 推送 2026-09-14 · [GitHub](https://github.com/sonnvntu/openviewer-releases) · [官网](https://aiopenviewer.com/) · 组织维护 · 中文 README

**带 AI 视觉检测的跨平台远程桌面与摄像头监控工具**

面向个人远程访问场景的客户端/主机架构软件：通过 P2P（DTLS 加密、STUN/TURN 穿透 NAT）远程查看与控制计算机，支持屏幕流、多显示器、文件传输，覆盖 Windows/Linux/macOS/Android/iOS。AI 部分接入网络摄像头或 IP 摄像头，可部署自定义 ONNX/NCNN 模型（CPU 或 Vulkan GPU 加速），执行检测→分类→规则→告警的流水线，识别人、火情、车辆等事件并推送通知。各平台以安装包（exe/AppImage/deb/dmg/apk）从 GitHub Releases 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 远程桌面 + 摄像头 AI 检测（人/火情/车辆等事件）一体化
- 自定义 AI 模型部署，CPU 与 Vulkan GPU 加速
- Detection→Classification→Rule→Alert 可视化 AI 工作流
- P2P 端到端加密（DTLS），NAT 穿透无需端口转发

## 适用场景

- 外出时远程查看并控制自己的电脑
- 通过摄像头监控设备周边环境，检测有人闯入或火情并收到推送
- 部署自己训练的检测模型实现定制化告警

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L23: That's why OpenViewer is built differently. Instead of just a Remote Access tool, OpenViewer connects webcams or IP
> L32: - 📹 **AI-Powered Vision** — Transform cameras into intelligent sensors.

## 星数曲线

```mermaid
xychart-beta
    title "sonnvntu/openviewer-releases 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8fcbaee5cea2` · [字段定义](../../DATASET.md)*
