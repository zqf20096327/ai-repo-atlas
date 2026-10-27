# InternLM/Challenge-Cup-2026

⭐ 25 · Python · 推送 2026-08-06 · [GitHub](https://github.com/InternLM/Challenge-Cup-2026) · 组织维护 · 中文 README

**挑战杯 AI 赛道初赛 baseline：数学推理智能体接口与调试框架**

InternLM 维护的挑战杯人工智能赛道初赛 baseline 仓库：围绕 Intern-S 系列模型设计数学推理智能体。规定提交规范——根目录 user_agent.py 提供 ReasoningAgent 类，实现 solve(problem, metadata) 返回含 final_response 的字典；模型调用由平台官方 client 管理，禁止硬编码 API key。附本地 runner（JSONL 输入、逐题落盘、近似 3 题并发）与书生 API 控制台接入说明。正式评测用隐藏测试集，单题 1200 秒、总 6 小时硬时限，限制为非流式单候选请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规定 ReasoningAgent 与 solve 接口规范及 final_response 输出格式
- 本地 runner 支持 JSONL 输入、断点续跑与可调并发
- 附 InternChatClient 参考，支持 thinking_mode/tools 参数透传
- 明确评测时限、提交次数（每天 2 次/每周 10 次）与判分流程

## 适用场景

- 参赛者基于 baseline 搭建并调试数学推理智能体
- 对照接口规范准备符合要求的提交仓库
- 使用样例数据本地验证安装、初始化与输出保存流程

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: 本仓库是挑战杯人工智能赛道初赛的 baseline 仓库。赛题围绕 Intern-S 系列模型的数学智能体设计与推理创新展开，选手需要设计一个能够解决数学问题的推理智能体。智能体接收一道数学题文本，结合题目元信息进行推理，并输出最终
> L8: agent.solve(problem: str, metadata: dict) -> dict
> L25: 本仓库提供一个 naive agent baseline，作用是帮助选手理解：

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/Challenge-Cup-2026 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5fd72b3e0dbb` · [字段定义](../../DATASET.md)*
