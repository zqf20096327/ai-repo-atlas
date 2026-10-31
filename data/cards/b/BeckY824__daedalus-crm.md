# BeckY824/daedalus-crm

⭐ 19 · TypeScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/BeckY824/daedalus-crm) · [官网](https://ai-daedalus.com) · 组织维护 · 中文 README

**本地优先的桌面端 AI CRM，AI 起草、人确认写入**

面向个人销售、个体户与小团队的 Mac/Windows 桌面端客户管理系统：线索→客户→跟进→商机→签约全流程，推荐归属自动计算。首页是 ReAct 循环的 agent 对话面，模型自行调用只读工具查询，改动以建议卡形式呈现、人工确认才落库；支持粘贴聊天切分导入客户、整理跟进记录。AI 走 OpenAI 兼容接口，一键配置 DeepSeek，也可用自有 Key 或经 MCP 接 Claude Code/Codex。个人版免费，团队版按席位收费，同步内容端到端加密。数据为本机 SQLite 文件，断网可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct agent 对话面：模型自行决定调用只读工具，逐步可见
- AI 只出建议卡，人确认才写入，写操作走相同 server action 并留痕
- 粘贴聊天/Excel 导入客户，AI 只切分不推断，整批可撤销
- 个人版免费、数据本机 SQLite 单文件，团队版加密同步、按席位收费

## 适用场景

- 个体销售或一人公司在自己电脑上管客户，断网也能用
- 小团队各自用桌面端，客户与商机自动加密同步
- 把微信里转来的名单粘贴进 AI 切成客户表核对入库

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: **桌面端客户管理系统（Mac / Windows）**：线索 → 客户 → 跟进 → 商机 → 签约，推荐归属自动算。
> L41: - ✅ 也可以**不用我们的 AI**：让 Claude Code / Codex 通过 MCP 连进来，用你自己的订阅额度查你自己的库
> L35: **100% 开源 &nbsp;·&nbsp; 数据在你自己的电脑上 &nbsp;·&nbsp; AI 只起草，写入永远由人点**

## 星数曲线

```mermaid
xychart-beta
    title "BeckY824/daedalus-crm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `39263a1bb02b` · [字段定义](../../DATASET.md)*
