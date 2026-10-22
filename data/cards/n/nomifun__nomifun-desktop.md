# nomifun/nomifun-desktop

⭐ 303 · Rust · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/nomifun/nomifun-desktop) · [官网](https://www.nomifun.com) · 个人维护 · 中文 README

**本地优先的开源 AI 工作站桌面应用，数据不出本机**

基于 Tauri 2 + Rust 后端 + React 前端的本地 AI 工作站：一个后端同时支撑 Tauri 桌面应用与 WebUI。用户配置自己的模型服务商，功能覆盖对话与任务感知路由、无人值守自动化、统一知识库、原生电脑/浏览器操作、MCP 与技能扩展、终端/SSH 会话、应用托管与远程治理 API。无云账号、无遥测，工作区数据保持本地，请求仅发往用户配置的模型服务。Apache-2.0 许可，明确允许商用与分叉；维护者声明为业余维护、部分功能未包含在开源版本中，并提示迭代期间存在数据风险、升级前需备份。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 Rust 后端同时支撑 Tauri 桌面应用与桌面级 WebUI
- 数据本地存储、无遥测、无云账号，模型调用指向用户配置的服务
- 覆盖 Agent 自动化、Computer/Browser Use、MCP 与技能扩展、终端/SSH、应用托管
- Apache-2.0 许可，明确允许商用与分叉

## 适用场景

- 在本机搭建带 Agent 自动化与知识库的个人 AI 工作站
- 配置自有模型服务商并按任务路由调用
- 通过 MCP、技能与终端/SSH 扩展和驱动桌面自动化
- 以 Docker 自托管 Web 版并暴露治理 API

## 场景标签

`AI 助手` `GUI 自动化` `知识库管理` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L34: **NomiFun** is everything you imagine an AI workstation to be — and it runs on your terms. One React frontend and o
> L40: NomiFun Desktop is a local AI workstation with one Rust backend shared by a Tauri desktop
> L47: |Chat with configured providers, local models and task-aware routing|Models and routing, Agents and presets|

## 星数曲线

```mermaid
xychart-beta
    title "nomifun/nomifun-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 298 --> 304
    line [299, 302, 303]
```

2026-10-18 299 → 2026-10-22 303（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4c9bd0daced8` · [字段定义](../../DATASET.md)*
