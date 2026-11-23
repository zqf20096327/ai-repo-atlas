# arrow1031-dev/dsh-qq-bot

⭐ 11 · JavaScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/arrow1031-dev/dsh-qq-bot) · 个人维护 · 中文 README

**把 QQ 消息接入 DSH Agent 的插件，每会话独立**

面向 DSH（DeepSeek Harness）用户的 QQ 接入插件：经 OneBot 11/12、Satori、Milky 或 QQ 官方机器人协议端收发消息，每个群聊/私聊映射为独立 DSH 会话，落盘并可在 Web UI 打开。插件向 DSH 注册 10 个工具（联网搜索、抓网页、图片反搜、生图、表情包、群管理等），带权限四路并集与 fail-closed 白名单机制。仅一条运行时依赖，须 Node ≥22.6；不含协议端，需自行部署并按 npm 包安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套插件支持五种接入协议，切换仅需改设置
- 每个群/私聊是独立 DSH 会话，可在 Web UI 继续聊
- 注册 10 个 Agent 工具：搜索、抓网页、反搜、生图、群管理等
- 权限四路取并集，未配置 owners 时不驱动任何会话

## 适用场景

- 让 DSH Agent 在 QQ 群里回答消息、联网搜索并发图
- 通过 QQ 指令做群管理与权限控制
- 把已有 DSH 会话延伸到私聊继续使用

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: **把 QQ 接进 DSH：消息进来交给 Agent，回复发回 QQ。**
> L17: - **一套插件接五种协议**：OneBot 11（默认）/ OneBot 12 / Satori / Milky / QQ 官方机器人，换协议只是设置里的一个下拉。
> L169: 插件向 DSH 注册 10 个工具（访客只看到白名单里的）：

## 星数曲线

```mermaid
xychart-beta
    title "arrow1031-dev/dsh-qq-bot 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-11-22", "2026-11-23"]
    y-axis "stars" 2 --> 12
    line [3, 10, 11]
```

2026-10-29 3 → 2026-11-23 11（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `7ee470797736` · [字段定义](../../DATASET.md)*
