# mrliuzhiyu/Wechat-Claude-bot

⭐ 26 · Python · GPL-3.0 · 推送 2026-03-29 · [GitHub](https://github.com/mrliuzhiyu/Wechat-Claude-bot) · 个人维护 · 中文 README

**通过微信远程操控本机 Claude Code 的桌面客户端**

PyQt6 桌面客户端，通过微信官方 iLink Bot（ClawBot）协议扫码连接，用微信消息远程驱动本机 AI 引擎：默认 Claude Code CLI（stream-json 模式），可读写文件、执行终端命令、修改代码并实时推送操作进度到微信；另支持 Open Interpreter（多模型）与 Direct API（Anthropic/OpenAI/DeepSeek 纯对话）两个引擎。面向已持有 Claude Code 订阅、想在手机端远程开发/运维的用户。具备多用户会话隔离、会话持久化、文件双向收发（上限 50MB）、语音转文字与斜杠命令；本机运行，代码不经过第三方服务器。限制：并发上限 3，单次请求 5 分钟超时，Claude Code 以完整权限运行需信任发消息者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 微信消息远程驱动本机 Claude Code CLI，实时推送读文件/执行命令进度
- 三种 AI 引擎可切换：Claude Code / Open Interpreter / Direct API
- 基于 iLink Bot 协议长轮询，退出微信后消息排队，Bot 7×24 运行
- 多用户会话隔离与 sessionId 磁盘持久化，重启不丢上下文

## 适用场景

- 通勤路上用微信让 AI 修线上 Bug、改代码
- 手机端查看项目架构、做代码审查
- 远程执行 docker 等运维命令并查看结果
- 已有 Claude Code 订阅时零额外 Token 费用获得微信远程入口

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L17:  微信发消息 → AI 操控你的电脑 → 结果发回微信
> L130: 2. 将消息转发给当前选择的 AI 引擎（默认 Claude Code CLI，stream-json 模式）
> L186: 在微信中直接用自然语言描述你的需求，Claude Code 会自动执行：

## 星数曲线

```mermaid
xychart-beta
    title "mrliuzhiyu/Wechat-Claude-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b38d59e5c1c9` · [字段定义](../../DATASET.md)*
