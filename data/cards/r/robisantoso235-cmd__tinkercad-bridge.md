# robisantoso235-cmd/tinkercad-bridge

⭐ 3 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/robisantoso235-cmd/tinkercad-bridge) · 个人维护

**让 AI agent 通过 Chrome 扩展驱动本机浏览器的本地桥接服务**

由三部分组成：监听 127.0.0.1:8787 的 Node HTTP 队列服务、通过 chrome.debugger（CDP）执行命令的 Chrome MV3 扩展、以及供 agent 每次调用一个进程的 CLI（ab.mjs）。复用用户已登录的 Chrome 会话与真实标签页，不使用 Playwright 或 Chrome for Testing，不改动 Chrome profile。核心命令通用（点击、拖拽、截图、DOM 读取），并为 Tinkercad、Logicly、Canva 提供专用 helper；Logicly 命令作用于编辑器模型而非像素坐标。无 npm 依赖，仅需 Node 18+ 与 Chrome 116+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复用本机 Chrome 已登录会话，无需重新登录或分离 profile
- 三组件架构：HTTP 队列服务 + CDP 扩展执行器 + 无状态 CLI
- Logicly 命令操作编辑器模型（对象/终端/连线/信号）而非像素
- 安全限制：仅监听 127.0.0.1、Host/Origin 校验、不存储凭据

## 适用场景

- 让 AI agent 操作我已登录的网页应用（如 Tinkercad、Canva）而不用重新登录
- 通过五分钟清单把桥接扩展到其他允许的网站
- 用 CLI 命令在 Logicly 中搭建并验证电路模型

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Kendalikan **Chrome milikmu sendiri** dari agent AI — memakai sesi login yang sudah ada.
> L13: Bridge ini generik: bisa dipakai untuk **situs apa pun** yang kamu izinkan. Tiga situs yang
> L236: |`bridge-server.mjs`|Antrean perintah + hasil, HTTP|Node, background|
> L238: |`ab.mjs`|CLI untuk agent|Dipanggil per perintah|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2b7ec00eb9e7` · [字段定义](../../DATASET.md)*
