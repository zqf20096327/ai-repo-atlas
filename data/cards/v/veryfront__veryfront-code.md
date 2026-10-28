# veryfront/veryfront-code

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/veryfront/veryfront-code) · [官网](https://veryfront.com/docs/code) · 组织维护

**TypeScript/React 全栈框架：单项目构建 AI 应用与 Agent**

开源全栈框架，将 React 路由、Agent 定义、Zod 类型化工具、evals、多步工作流统一在文件式 TypeScript 项目中，开发者与编码 Agent 共用同一套约定。支持 Node.js/Deno/Bun 三种运行时，可直连模型提供商或 OpenAI 兼容本地服务，也可经 Veryfront Cloud AI Gateway 托管访问；支持自托管无需账号。能力包括多 Agent 编排、MCP Server、沙箱、知识文件与 Redis 持久化检查点，并提供七个起步模板。Apache-2.0 许可。

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

- 文件式项目统一组织 Agent、工具、工作流与 React 页面
- 同一项目可运行于 Node.js、Deno、Bun
- Zod 类型化工具自动从文件发现，无需手动注册
- 内置 MCP Server（SSE、会话、elicitation）与沙箱执行环境

## 适用场景

- 用 TypeScript 构建带聊天 UI 和工具调用的 AI Agent 应用
- 搭建多 Agent 协作或多步骤审批工作流
- 通过 MCP 向编码 Agent 暴露项目工具与实时诊断

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: Veryfront Code is an open-source, full-stack framework that keeps React routes,
> L27: Build agents, workflows, and full-stack React applications from one TypeScript project.

## 星数曲线

```mermaid
xychart-beta
    title "veryfront/veryfront-code 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `937bf2923c48` · [字段定义](../../DATASET.md)*
