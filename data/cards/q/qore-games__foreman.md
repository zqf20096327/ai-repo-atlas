# qore-games/foreman

⭐ 3 · Kotlin · MIT · 推送 2026-11-23 · [GitHub](https://github.com/qore-games/foreman) · [官网](https://qore-games.github.io/foreman/) · 组织维护

**Minecraft 服务器管理者的多合一调试工具，带游戏内 AI 助手**

面向 Minecraft 服务器管理者、管理员与插件开发者的 Fabric 客户端模组（可选 Paper 服务端插件），支持 Minecraft 26.2/26.3。核心功能：数据包查看器（记录与归组服务器/客户端流量）、HUD 检查器、插件位置在世界内绘制、快速资源包重载、复制物品检测与世界编辑工具。AI 部分：游戏内聊天基于用户自己的 Claude Code、opencode 或 OpenRouter 账户运行，可截图、执行命令、读写指定文件夹；并通过 MCP 服务器（默认 127.0.0.1:25599）让终端中的外部 agent 操控客户端。生产环境可用 preset: production 限定为只读工具且不开端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据包查看器：按来源归组流量并给出插件内搜索线索
- 游戏内 AI 聊天使用用户自己的 Claude Code / opencode / OpenRouter 账户
- MCP 服务器让外部 agent 获取截图、HUD、实体、数据包并执行命令
-  Skills 机制：插件开发者用 markdown 文件向 AI 教授自己的插件命令

## 适用场景

- 在运行中的服务器上排查数据包洪水与插件 bug
- 让 AI 在游戏内代为修配置、重载插件并验证结果
- 上线前用 AI 复现菜单/商店的物品复制漏洞
- 在编辑器写插件、由外部 agent 在运行的游戏中端到端测试

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L5: A multi-tool for Minecraft server owners, admins and plugin developers. See what your server sends and draws, debug
> L95: - **Chats in game.** Ask in plain words. The AI runs on your computer with your own Claude Code, opencode or OpenRo


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `0d41be3f969a` · [字段定义](../../DATASET.md)*
