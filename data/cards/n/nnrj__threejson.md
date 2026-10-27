# nnrj/threejson

⭐ 39 · JavaScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/nnrj/threejson) · [官网](https://threejson.org/) · 组织维护 · 中文 README

**JSON 驱动的 Three.js 声明式场景运行时，供人与 Agent 构建 3D 世界**

面向 Three.js 开发者的 JSON 声明式场景运行时：以 JSON 配置描述场景，运行时负责解析并构建，替代手写 Three.js 代码；场景可持久化、可变更、可扩展。设计支持 AI/Agent 生成与控制场景（Agent as Operator），提供 JSON Patch 接口修改场景，域（domains）机制支持业务扩展。以 npm 包提供，可选能力包（归档/GIF/CSG/SDF 文本）按需安装；也可克隆仓库配合静态服务器无构建使用。商标与源码许可分离，源码为 MIT。

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

- JSON 配置驱动构建 Three.js 场景，替代手写样板代码
- Agent as Operator：面向 AI/Agent 的场景生成与控制，含 JSON Patch 接口
- 域（domains）扩展机制与窄入口/聚合入口分层导入
- 静态资源默认 CDN 回退（jsDelivr），支持本地挂载

## 适用场景

- 用 JSON 配置而非手写 Three.js 代码搭建 3D 场景
- 让 AI Agent 生成和修改可持久化的 3D 世界
- 通过自定义业务域扩展场景运行时

## 场景标签

 · 领域:Web 3D 图形/场景运行时

## 证据(README 行号)

> L8: JSON-driven Three.js scene runtime: build 3D scenes from configuration instead of hand-writing large chunks of Three
> L20: ThreeJSON is a JSON-driven declarative scene runtime for Three.js, designed for persistent, mutable and extensible 
> L68: > **Agent as Operator** — Agents are operators.

## 星数曲线

```mermaid
xychart-beta
    title "nnrj/threejson 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9181a2f25b55` · [字段定义](../../DATASET.md)*
