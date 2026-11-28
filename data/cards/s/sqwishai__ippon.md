# sqwishai/ippon

⭐ 59 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/sqwishai/ippon) · 组织维护

**macOS 本地决策模型运行时：输出概率化判断结果**

面向 Apple silicon Mac 的本地决策模型推理运行时，提供 CLI（ippon decide）、Python API（ippon.Decider）与本地 HTTP 服务（ippon serve）三种使用方式，输出 yes/no 概率、选项概率与分数，支持文本/图像/音频/视频输入。每个模型构建按发布者参考代码做概率容差校验（ippon verify / eval）。通过 install.sh、pip 或源码安装；模型下载需按许可确认，Kettei 系列采用社区模型许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI、Python API 与 HTTP 服务三种调用方式，输出概率化决策结果
- 支持 noul/choice/score 三类问题及多模态输入（图像/音频/视频）
- MCP 服务器与 Claude Code、Codex、OpenCode、Pi、Cursor 等 agent 宿主接入
- 按创建者参考代码做概率容差校验与阈值评估（ippon verify/eval）

## 适用场景

- 在 Mac 本地对客服消息做退款/分类的概率判断
- 为多个 agent 共享一个本地决策模型服务
- 用自标注样本评估决策模型的阈值可靠性

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12: **Run decision models on your Mac, blazing fast,** down to **51 ms** text (14 ms on cached context), **39 ms** audi
> L124: To share one model with every app and agent on your Mac, serve it. In a terminal, `ippon serve kettei-core` prints
> L193: From another process, language, or the Sqwish Labs SDK, `ippon serve` answers the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `87ec0ed8c586` · [字段定义](../../DATASET.md)*
