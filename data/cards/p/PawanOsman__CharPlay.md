# PawanOsman/CharPlay

⭐ 20 · TypeScript · NOASSERTION · 推送 2026-09-15 · [GitHub](https://github.com/PawanOsman/CharPlay) · [官网](https://play.pawan.krd) · 个人维护

**AI 角色聊天 Playground：本地存储、Socket.IO 在线状态、可插拔模型后端**

基于 Next.js 16 / React 19 / Tailwind CSS 4 的 AI 角色聊天 Web 应用，面向角色扮演聊天用户。提供浏览器本地会话存储、Socket.IO 在线状态、可插拔模型后端：服务器端使用 PAWANKRD 凭证的托管聊天/模型端点，浏览器端保留自带 key 的 provider。含速率配额、origin 校验、安全测试套件与 Docker 部署（非 root、只读文件系统）。生产服务端口 6328 或 Compose 的 3000，需 Node.js 22.13+/24 LTS 与 pnpm 11.14.0。许可证为 CC BY-NC-SA 4.0（含非商业条款）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地会话存储与 Socket.IO 在线状态
- 可插拔模型后端：托管 provider 与浏览器端自带 key 两种路径
- 配套 HTTP 安全集成测试与安全审计命令
- Docker Compose 部署（非 root 用户、只读文件系统、丢弃 capabilities）

## 适用场景

- 自部署一个 AI 角色扮演聊天站点
- 用自带 API key 在浏览器侧与角色模型对话
- 通过 Docker 在服务器上托管多人聊天 playground

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: # CharPlay (AI Character Playground)
> L3: An AI character chat playground with local conversation storage, Socket.IO presence, and a pluggable model backend. 
> L17: Open http://localhost:3000. Development binds to localhost. Set the provider key in `.env` to enable the hosted cha

## 星数曲线

```mermaid
xychart-beta
    title "PawanOsman/CharPlay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b1dea2d7cbaa` · [字段定义](../../DATASET.md)*
