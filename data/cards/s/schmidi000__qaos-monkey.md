# schmidi000/qaos-monkey

⭐ 21 · TypeScript · MIT-0 · 推送 2026-07-30 · [GitHub](https://github.com/schmidi000/qaos-monkey) · [官网](https://qaosmonkey.com/) · 个人维护

**驱动 iOS/Android 模拟器的探索式移动测试 AI agent**

技术栈无关的探索式移动测试代理：通过 agent-device 控制 iOS 模拟器与 Android 模拟器，向可配置的模型（Codex CLI/Claude Code 等命令行，或 OpenAI 兼容、Anthropic API）询问下一步动作，结合视觉语言模型与系统无障碍树感知 UI；遇到登录、验证码等阻碍时暂停等待人工介入（HITL）后恢复。采用 LangGraph 状态机，支持 coverage-guided 确定性覆盖引导策略，输出含截图与步骤轨迹的可复现报告，凭据在写入前会被脱敏。需要 Node.js 22.6+、Xcode/Android 模拟器及一个模型提供方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VLM + OS 无障碍树双通道感知 UI，对轻微界面改动不敏感
- Human-in-the-Loop 断点：遇登录/验证码等暂停，人工协助后恢复
- coverage-guided 确定性覆盖引导策略：拒绝过早结束、避免重复无效动作、按界域回溯
- 生成含截图、步骤轨迹的 report.md/report.json，凭据写入前脱敏

## 适用场景

- 在模拟器上对我开发的 App 做探索式冒烟测试找 bug
- CI/CD 中替代脆弱的 XPath 脚本式 UI 测试
- 让 agent 尝试以对抗方式破坏我的移动应用并产出可复现报告

## 场景标签

 · 领域:移动测试/QA 自动化

## 证据(README 行号)

> L5: QAosMonkey is a tech-agnostic exploratory mobile testing agent. It drives iOS and Android emulators through `agent-d
> L15: **QAosMonkey bridges this gap.** By combining Vision-Language Models (to see the UI like a human) with the OS acces

## 星数曲线

```mermaid
xychart-beta
    title "schmidi000/qaos-monkey 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6914b5c59167` · [字段定义](../../DATASET.md)*
