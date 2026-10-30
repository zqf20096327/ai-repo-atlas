# Sjeary/ShareGPT

⭐ 15 · JavaScript · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/Sjeary/ShareGPT) · [官网](https://github.com/Sjeary/ShareGPT/releases) · 个人维护 · 中文 README

**把 ChatGPT/Claude/Gemini 装进一个客户端的团队协作桌面应用**

基于 Electron 的跨平台桌面工作区，内嵌 ChatGPT、Claude、Gemini 网页分区，配合基于 sing-box 的代理线路管理（管理员可按 AI 指定默认出口）、翻译工作台、日历、待办、Markdown 知识库、番茄钟和本机终端。提供个人工作区（本机自用）与团队工作区（连接自托管 Node.js 协作服务端，管理员统一下发网络与翻译配置、管理权限与用量）两种隔离模式。不附带公共服务器、代理节点或第三方 AI 账号，需自建或自带。支持 Windows x64 与 macOS Apple Silicon 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内嵌 ChatGPT/Claude/Gemini 独立网页分区，登录状态本机保存
- 基于 sing-box 的代理管理，管理员可按 AI 分别指定默认线路并做代理检测
- 自托管协作服务端与管理控制台：账号、聊天、权限、托管翻译与用量统计
- 本地 Markdown 知识库（双链/图谱/Canvas）与 Notes AI 扩写/问答

## 适用场景

- 团队统一配置代理线路，成员在客户端内使用 ChatGPT/Claude/Gemini
- 个人在本机集中使用 AI 网页、翻译与笔记/日历工具
- 小组通过自托管服务端进行聊天、组队日历与用量管理

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L16: ShareGPT 是一个面向 AI 网页使用、个人知识管理和小团队协作的桌面工作区。它提供两种彼此隔离的使用方式：个人工作区无需团队账号，代理、翻译接口和 AI 网页登录状态只保存在本机；团队工作区连接你或组织自托管的协作服务器，
> L24: - **桌面客户端**：内嵌三家 AI 网页，并提供翻译、日历、待办、知识库、专注工具、个人网络配置和可选的团队协作。

## 星数曲线

```mermaid
xychart-beta
    title "Sjeary/ShareGPT 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `261e5e880f22` · [字段定义](../../DATASET.md)*
