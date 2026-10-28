# etairl/Probus

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/etairl/Probus) · 个人维护

**开源 AI 漏洞扫描器：用开源模型扫描代码供应链**

面向开发者的代码库与供应链安全扫描工具，由三个 agent 组成：Analyst 挑选关键文件、Researcher 逐文件追踪调用链产出原始发现、QA 独立验证攻击向量并生成报告。每个发现附带漏洞代码、攻击路径与一键修复建 PR 操作。通过 npm 全局安装后启动本地 Web 服务器，在浏览器中完成选仓库、填模型 API key、查看实时流水线仪表盘。模型主要经 OpenRouter 使用开源模型，也可配置 OpenAI/Anthropic；主次双模型分工控制成本，每文件约消耗 100 万输入 token。

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

- Analyst/Researcher/QA 三 agent 流水线，QA 独立验证每个发现
- 每个发现附漏洞代码、攻击路径与一键 Fix→PR
- 本地 Web UI 驱动，API key 存于本机 ~/.probus/.env（chmod 600）
- 主/次双模型分工（约 90%/10% token）控制扫描成本

## 适用场景

- 扫描自有代码库找出潜在漏洞与攻击路径
- 开源维护者做供应链安全检查
- 基于扫描报告一键提交修复 PR

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: > Open-source AI vulnerability scanner powered by open models.
> L17: Probus harnesses 3 agents that:
> L52: Probus runs most (cost) effectively with open models using OpenRouter. It is still possible however to use other pr

## 星数曲线

```mermaid
xychart-beta
    title "etairl/Probus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e18ecc3f836` · [字段定义](../../DATASET.md)*
