# Hxin725/claude-web-test-harness

⭐ 44 · Python · MIT · 推送 2026-11-03 · [GitHub](https://github.com/Hxin725/claude-web-test-harness) · 个人维护 · 中文 README

**Claude Code 驱动的多 agent UI 测试编排骨架**

供 Web 项目使用的测试编排骨架：交给它 PRD（或仅有网站地址），它把需求拆成 7 类检查清单，在本机启动测试台账网页供人工逐卡确认，再生成正式用例、编写 pytest-playwright 自动化、执行并把结果写回台账。本体是一组 markdown 指令 + 普通 pytest-playwright 项目，需外部 AI 编码工具充当调度器：Claude Code 原生支持，Codex/CodeBuddy 等可用兼容提示词以单 agent 串演各角色运行。无配置文件，靠目录约定与 CLAUDE.md 适配项目；不含业务概念。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 需求→清单→用例→自动化→审查的多角色流水线，通过文档交接
- 本地测试台账网页逐卡人工确认，决策点一律暂停等待
- 7 类清单分解（功能/字段/状态迁移/业务规则/用户旅程/影响范围/元素规格）
- Claude Code 原生支持，其他 agent 工具可用兼容提示词运行

## 适用场景

- 有 PRD 的 Web 功能按需求先行生成并评审测试用例
- 无需求文档时让 agent 先探索页面再设计测试
- 接入手头已有 pytest-playwright 项目做 AI 编排测试

## 场景标签

`多智能体` `浏览器自动化` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: A multi-agent UI testing framework driven by Claude Code. Drop it into your Web project and hand it a requirement do
> L107: This harness relies on an **AI coding tool** to act as the "dispatcher" — it's responsible for
> L109: is just **a pile of markdown instructions + an ordinary pytest-playwright project**; it isn't

## 星数曲线

```mermaid
xychart-beta
    title "Hxin725/claude-web-test-harness 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 42 --> 45
    line [43, 44]
```

2026-11-08 43 → 2026-11-28 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `e05de652d273` · [字段定义](../../DATASET.md)*
