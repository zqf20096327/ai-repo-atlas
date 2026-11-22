# HKUDS/DeepCode

⭐ 16,859 · Python · MIT · 推送 2026-11-17 · [GitHub](https://github.com/HKUDS/DeepCode) · [官网](http://arxiv.org/abs/2512.07921) · 组织维护 · 中文 README

**开源多智能体编码 Agent：理解项目、改代码并验证完成**

面向真实软件工程的开源 Coding Agent：给定小改动或数十步的长期目标，它读取与编辑文件、运行命令与测试、以 diff 展示修改，并用确认的检查清单与可选独立评审来验证完成声明；Goal 与会话由本地后台服务持久化，可在 TUI、Desktop、Web 与 headless 四种客户端间延续。机制上含压缩保词上下文、卡死自动停止、权限分级与 OS 沙箱；自进化（从验证过的运行中学习）为规划中特性，尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 3.8 天,年发版 12,33 位贡献者
- 涨星:近 1 天 **+9**(自 20261016 起算)
- 平台:— · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- Verified completion：运行确认清单并由独立评审以证据证明每条需求
- 本地后台服务持久化 Goal/会话，四种客户端共享同一服务
- 14 个内置 provider 模板，兼容 OpenAI/Anthropic API 与本地模型
- MCP 接入（stdio/SSE/Streamable HTTP），并可把自身暴露为 MCP 服务器

## 适用场景

- 让 Agent 在真实仓库中完成跨多轮的重构或修 bug 任务
- 脚本/CI 中以 headless 方式跑一轮编码任务并收集 NDJSON 事件
- 把论文或技术文档转成代码库（Paper2Code）
- 定时自动运行保存的指令（Automations）

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L78: DeepCode is an open-source Coding Agent for real software engineering. Give it
> L115: - **One session, four clients.** Turns run in a local background service,
> L236: |Model|An API key for a supported provider, or a local Ollama or vLLM server. The model must support tool calling;

## 星数曲线

```mermaid
xychart-beta
    title "HKUDS/DeepCode 星数(近 23 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 16720 --> 16871
    line [16732, 16739, 16744, 16746, 16753, 16758, 16763, 16770, 16776, 16779, 16781, 16753, 16823, 16835, 16838, 16842, 16844, 16845, 16849, 16851, 16853, 16857, 16859]
```

2026-10-20 16,732 → 2026-11-22 16,859（+127）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c1e2ff975795` · [字段定义](../../DATASET.md)*
