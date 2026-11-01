# Xpropel/Pi-Remote

⭐ 154 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/Xpropel/Pi-Remote) · 个人维护 · 中文 README

**把 pi 终端编码代理会话镜像到浏览器的远程控制工具**

构建于 pi 官方扩展 API 之上的伴侣工具：在 pi 进程内运行同步扩展，将终端会话实时镜像到浏览器，可发送消息、切换模型/思考级别、压缩上下文、创建/克隆会话并查看 token 与费用。会话始终保留在本地 pi 进程，浏览器仅作镜像与控制面。中继服务自托管，端到端使用双 token 认证，支持局域网直连、QR 设备配对与按需 Cloudflare Tunnel。为个人单用户设计，无多用户权限系统；需先自行安装 pi，Node ≥ 22.18。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 pi 官方扩展 API 镜像会话，不修改 pi 源码
- 远程命令：切换模型、思考级别、压缩上下文、会话树导航
- QR 设备配对与多设备共享一个自托管中继
- 双 token 认证、远程 bash 默认禁用、会话内容默认不持久化

## 适用场景

- 在手机上查看并操控本机运行的 pi 编码会话
- 离家时通过 Cloudflare Tunnel 临时公网访问自己的会话
- 同时管理多台机器上的 pi 设备与会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Pi-Remote attaches to a running pi session through pi's official extension API. It does not modify pi's source code
> L15: > **Relationship to pi**: Pi-Remote is a companion tool built for pi, Earendil's terminal coding agent, on pi's off


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f1a63634c361` · [字段定义](../../DATASET.md)*
