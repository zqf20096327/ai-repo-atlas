# HydroRoll-Team/DropOut

⭐ 22 · Rust · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/HydroRoll-Team/DropOut) · [官网](https://dropout.hydroroll.team) · 组织维护 · 中文 README

**用 Rust/Tauri 打造的可复现 Minecraft 启动器，含可选 AI 助手**

面向开发者的桌面 Minecraft 启动器，核心概念是把游戏环境当作可版本化的 workspace 管理：Rust 核心负责认证、下载、Java/版本解析与实例存储，React 19 UI 经 Tauri 2 命令渲染。功能覆盖微软 OAuth 登录、隔离实例系统、Fabric/Forge 安装、自动内存分配、并发下载、Monaco 配置编辑器；另提供可选的本地或 OpenAI 兼容的故障排查助手。提供 Windows/macOS/Linux 多平台预构建安装包，运行不需要 Rust 或 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实例隔离：每实例独立目录、备注、内存/Java 覆盖与迁移入口
- 按实时 RAM 与模组数量自动分配堆内存并保留系统余量
- 可选的本地或 OpenAI 兼容游戏助手，处理日志/崩溃/配置问题
- 预构建安装包带签名 GitHub build provenance，可验证构建来源

## 适用场景

- 把每个 Minecraft 模组环境当作可追溯、可复现的工作区来管理
- 一站式完成登录、Java 运行时、版本与 Fabric/Forge 加载器安装
- 用 AI 助手排查游戏日志、崩溃与配置问题

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L25: **DropOut** is a modern, developer-grade Minecraft launcher built around one idea: a game setup should be traceable

## 星数曲线

```mermaid
xychart-beta
    title "HydroRoll-Team/DropOut 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `53b8c7bb715b` · [字段定义](../../DATASET.md)*
