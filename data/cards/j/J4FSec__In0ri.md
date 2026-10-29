# J4FSec/In0ri

⭐ 64 · CSS · AGPL-3.0 · 推送 2026-07-17 · [GitHub](https://github.com/J4FSec/In0ri) · 组织维护

**用深度学习检测网页篡改并告警的自动化监控系统**

面向 Web 应用安全运维的网站篡改（defacement）检测系统：定时对目标网站截图，由训练好的模型识别页面视觉异常与篡改模式，检测到被篡改页面后通过 Email 或 Telegram 告警。提供 WebUI（docker-compose 部署，端口 8080），支持两种监控方式：Celery Beat 周期性访问 URL 截图检测，或在被监控 Web 服务器上部署内部 Agent 扫描文件目录。曾在 Black Hat Europe 2021 / Asia 2022 / USA 2022 展示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截图模拟真实用户行为，由训练模型识别视觉篡改异常
- Email 与 Telegram 告警通道
- URL 周期检测与服务器内部 Agent 两种部署方式
- docker-compose 一键部署并自带 WebUI

## 适用场景

- 监控企业网站是否被篡改挂马并及时收到告警
- 对多个目标 URL 做集中式可视化篡改检测
- 在 Web 服务器上部署 Agent 扫描本地目录变更

## 场景标签

`网络安全` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L3: In0ri is an automated, AI-powered website defacement detection system.
> L6: In0ri acts as an intelligent watchdog for your web applications. Instead of relying on traditional source code monit

## 星数曲线

```mermaid
xychart-beta
    title "J4FSec/In0ri 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-29 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `572e2d09f2ad` · [字段定义](../../DATASET.md)*
