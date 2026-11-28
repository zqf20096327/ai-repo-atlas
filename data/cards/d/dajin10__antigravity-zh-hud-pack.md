# dajin10/antigravity-zh-hud-pack

⭐ 4 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/dajin10/antigravity-zh-hud-pack) · 个人维护 · 中文 README

**Antigravity 桌面客户端的中文汉化与 Token/配额监控拓展包**

面向 Antigravity 桌面客户端的增强拓展包，通过向 Electron `app.asar` 的 `preload.js` 注入模块实现三类功能：全量简体中文界面汉化（支持中/英/双语三态切换、自定义词典热加载）、输入框下方双行 HUD 状态栏（实时 Token 用量、生成速率 tok/s、上下文占比、5h/每周配额进度与倒计时）、任意文件拖拽注入磁盘绝对路径。数据全部本地处理，支持备份与一键无损卸载；客户端官方更新后需重跑安装脚本恢复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入框底部双行 HUD：实时 tok/s、Token/缓存命中、上下文环形占比、5h/每周配额进度与倒计时
- 全量简体中文汉化引擎，支持中英双语三态切换与自定义词典热加载
- 任意文件拖拽自动提取绝对路径插入输入框
- app.asar 备份与一键无损卸载还原

## 适用场景

- 中文用户将 Antigravity 界面切换为简体中文
- 实时监控 AI 会话的 Token 消耗与模型配额余量
- 拖入代码/日志文件时自动注入绝对路径到对话

## 场景标签

 · 领域:开发工具/客户端增强

## 证据(README 行号)

> L6: > 为 **Antigravity** 桌面客户端打造的一站式增强拓展包：集成 **中英双语 / 简体中文界面汉化 (v2.3.0)**、**输入框底部实时算力 / Token / 模型配额监控状态栏 (HUD)** 与 **全局文
> L116: Antigravity 是基于 **Electron**（内嵌 Chromium 渲染进程 + 本地 `language_server` 后端服务）构建的桌面客户端。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `5b49c0b2eb6d` · [字段定义](../../DATASET.md)*
