# 0x-elfateh1/claude-code-deepseek

⭐ 27 · Vim Snippet · MIT · 推送 2026-06-05 · [GitHub](https://github.com/0x-elfateh1/claude-code-deepseek) · 个人维护

**用 DeepSeek 的 Anthropic 兼容 API 运行 Claude Code 的配置指南**

面向安全研究人员与漏洞赏金猎人的配置指南仓库：通过设置 ANTHROPIC_BASE_URL/AUTH_TOKEN/MODEL 环境变量，将 Claude Code CLI 指向 DeepSeek 的 Anthropic 兼容端点。提供四种接入方式（全局环境变量、项目级 settings.json、shell 函数 claude-ds、CI 内联变量），支持 deepseek-v4-pro 主模型与 v4-flash 子代理模型自动映射，可用 unset 一条命令回退到 Anthropic 订阅。仓库本体是文档与 configs/ 配置片段，无可安装软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种接入方式：全局 / 项目级 / claude-ds shell 函数 / CI 内联变量
- claude-opus→v4-pro、claude-haiku/sonnet→v4-flash 的模型自动映射
- API key 无需浏览器 OAuth，适用 VPS/cron/CI 无头场景
- unset 变量即可回退 Anthropic 订阅，互不干扰

## 适用场景

- 在 VPS 或 CI 流水线中无头运行 Claude Code 做安全审计
- 用低成本 API 承载子代理等高频任务，保留订阅用于交互式编码
- 按项目或按会话切换 DeepSeek 与 Anthropic 两种后端

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > Run Claude Code CLI on DeepSeek's Anthropic-compatible API.
> L61: export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
> L167: ├── configs/

## 星数曲线

```mermaid
xychart-beta
    title "0x-elfateh1/claude-code-deepseek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a087e17cfc26` · [字段定义](../../DATASET.md)*
