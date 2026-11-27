# liuyanghejerry/Clausura

⭐ 205 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/liuyanghejerry/Clausura) · 个人维护 · 中文 README

**面向 CI/CD 流水线的 LLM agent CLI，用确定性规则给出门禁判定**

Clausura 是一个跨平台的 agent CLI 工具，嵌入 CI/CD 流水线：运行有界的 LLM agent 任务检查代码库，抽取结构化 findings，再用确定性门禁规则评估，以退出码 0/1/2/3 和 SARIF v2.1.0 输出 pass/fail，无人在环。提供 OpenAI 兼容、Anthropic 兼容与自定义三类 LLM 接入，支持 token/迭代/超时预算上限、fail-closed 策略、技能文件复用（渐进式加载）、findings 验证模型过滤，以及单二进制零运行时依赖部署。面向需要在流水线中获得可信任二元结论的工程团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 找问题、规则引擎判定、退出码+SARIF 报告的闭环执行
- max_iterations/timeout_secs/token_budget 等运行上界与 fail-closed 默认策略
- 三类 LLM 接入（OpenAI 兼容/Anthropic 兼容/自定义企业端点）
- 复用社区 Markdown 技能文件并按需加载以节省 token

## 适用场景

- PR 合并前用 LLM 代码审查结果做流水线门禁
- 跨仓库执行一致性与架构合规检查
- i18n 抽取与 locale 覆盖校验
- 按阈值只在超标时使流水线失败

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Clausura is a platform-agnostic agent CLI tool built for CI/CD pipelines. It runs bounded LLM agent tasks against y
> L31: If you are building an interactive coding agent, use a generic harness. If you need a *deterministic gate in CI* — 

## 星数曲线

```mermaid
xychart-beta
    title "liuyanghejerry/Clausura 星数(近 3 点)"
    x-axis ["2026-10-25", "2026-11-08", "2026-11-27"]
    y-axis "stars" 203 --> 206
    line [204, 205, 205]
```

2026-10-25 204 → 2026-11-27 205（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6e0e4757d8a2` · [字段定义](../../DATASET.md)*
