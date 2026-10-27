# Princeton-AI2-Lab/Avenir-Web

⭐ 32 · Python · Apache-2.0 · 推送 2026-03-12 · [GitHub](https://github.com/Princeton-AI2-Lab/Avenir-Web) · 组织维护

**多模态 Web Agent 框架：长程网页任务的可靠自主执行**

论文 "Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts" 的官方实现。提供自主网页代理框架，用于在复杂动态网页界面执行长程任务：组合 Mixture of Grounding Experts（MoGE）、Experience-Imitation Planning（EIP）与带任务追踪清单的自适应记忆。通过 Playwright（Chromium）驱动浏览器，模型经 OpenRouter API 接入；支持批量实验与单任务脚本两种运行方式，输出日志、截图与 LLM 记录等产物，并提供演示模式（光标可视化与实时仪表盘）。声明供研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MoGE + EIP + 任务追踪清单的模块化架构
- 支持单任务脚本与批量实验（TOML 配置）
- Demo Mode 提供光标可视化与实时仪表盘
- 每任务输出 agent.log、result.json、截图与 LLM 记录

## 适用场景

- 让 agent 在真实网站上完成多步骤长程任务
- 复现论文在 Online-Mind2Web 上的实验
- 录制高质量 agent 演示视频

## 场景标签

`Agent 框架` `浏览器自动化` · 领域:Agent 开发

## 证据(README 行号)

> L10: Avenir-Web is an autonomous web agent framework designed for reliable execution of long-horizon tasks on complex, d
> L119: This repository is provided for research use. Model outputs may be incorrect, incomplete, or unsafe; you are respo

## 星数曲线

```mermaid
xychart-beta
    title "Princeton-AI2-Lab/Avenir-Web 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 31 --> 34
    line [33, 32, 32]
```

2026-10-18 33 → 2026-10-27 32（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6575fb7543ad` · [字段定义](../../DATASET.md)*
