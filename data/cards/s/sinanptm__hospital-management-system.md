# sinanptm/hospital-management-system

⭐ 43 · TypeScript · 推送 2026-04-18 · [GitHub](https://github.com/sinanptm/hospital-management-system) · [官网](https://avm-ayurvedic.online) · 个人维护

**阿育吠陀医院的在线问诊平台：视频咨询、预约、支付与 AI 洞察**

面向阿育吠陀医疗场景的全栈 Web 平台（AVM Ayurvedic），前后端分离：Next.js/TypeScript 客户端，Node.js/Express/MongoDB 服务端。功能包括 WebRTC 视频咨询（Metered TURN 中继）、预约管理、Stripe 支付、Socket.io 实时通知、AWS S3 文件上传、Firebase 认证与邮件通知。AI 部分接入 Google Gemini API（需配置 GEMINI_API_KEY），README 标注 AI-Powered Wellness。需自配多个第三方服务后从源码运行，无桌面安装包或 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebRTC + Metered TURN 的视频咨询
- Stripe 支付网关集成与 webhook 监听
- 接入 Google Gemini API 提供 AI 功能
- AWS S3 文件上传与 Socket.io 实时通知

## 适用场景

- 医院或诊所搭建在线问诊与预约平台
- 通过视频咨询与聊天向用户交付远程医疗服务
- 在支付与通知流程中完成线上诊疗闭环

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L15: 📹 Video Consultations | 🤖 AI-Powered Wellness | 📅 Smart Booking | 💳 Secure Payments
> L52: Google AI
> L165: ### 3. Google Gemini AI

## 星数曲线

```mermaid
xychart-beta
    title "sinanptm/hospital-management-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `98c58edabd89` · [字段定义](../../DATASET.md)*
