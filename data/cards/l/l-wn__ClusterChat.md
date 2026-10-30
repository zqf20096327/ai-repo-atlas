# l-wn/ClusterChat

⭐ 23 · JavaScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/l-wn/ClusterChat) · [官网](https://clusterchat.io) · 个人维护

**浏览器内多人拼 GPU 分布式运行 27B 大模型的群聊应用**

纯浏览器运行的分布式 LLM 聊天应用：将模型按位置切成片段，多台设备的浏览器通过 WebRTC 手写 WebGPU 内核共同运行 Qwen3.8-27B（q8，约 27 GiB），无主机、成员可随时离开且回复不中断，单集群最多 64 人并发各自独立对话。支持投机解码、邀请码链接分片私密握手、IndexedDB 本地保存对话。限制：每集群单模型、仅聊天无 API/工具调用、对等端被信任、无硬件诚实性校验。自建需 Node.js/Python/Caddy 与 WebGPU 浏览器，公开使用则零安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型按位置切片由多浏览器经 WebRTC 共同运行，成员离开后回复可恢复
- 单集群支持最多 64 人，各自独立对话与分页 KV 缓存，可并发多个回复
- 邀请码存于 URL fragment 不经过服务器，WebRTC 握手签名，默认仅经中继隐藏 IP
- 投机解码每次环游最多校验 7 个 token，输出与关闭时逐位一致

## 适用场景

- 朋友、实验室或社团把多台机器的显存拼起来共同运行一个 27B 模型
- 跨地域多机（如法国+西班牙）通过浏览器组集群共同聊天
- 零安装：任何现代浏览器打开邀请链接即可加入聊天或出借 GPU

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L4: Cluster the graphics cards you already have to run a 27B model in the browser.
> L29: ClusterChat turns those machines into one model that the whole group uses at
> L83: |**ClusterChat**|browser tab (WebGPU)|yes, over WebRTC through a relay|none, open a link|yes, each person has their


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `99c8e5adca21` · [字段定义](../../DATASET.md)*
