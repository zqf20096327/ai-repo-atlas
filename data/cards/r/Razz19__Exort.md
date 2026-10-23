# Razz19/Exort

⭐ 226 · Svelte · AGPL-3.0 · 推送 2026-09-27 · [GitHub](https://github.com/Razz19/Exort) · [官网](https://exort.dev) · 个人维护

**面向微控制器的开源 AI 编程桌面工作区**

基于 Electron/Svelte 的嵌入式开发桌面应用，内置 OpenCode 驱动的 AI 编程代理，可检查工作区、解释代码、编辑文件；同时提供项目与开发板管理（基于 Arduino CLI）、编译上传、串口监视器与串口绘图仪，支持 Arduino/ESP32/ESP8266/RP2040/STM32/Teensy 等板卡。附带免费 OpenCode 模型，也可接入自有 OpenCode 兼容 provider。渲染进程经 preload IPC 与主进程通信。桌面版可从 exort.dev 或 GitHub releases 下载，也可用 Node.js 20+ 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenCode AI 代理：检查工作区、解释代码、编辑文件
- Arduino CLI 开发板平台管理与编译上传
- 串口监视器与数值串口绘图仪
- 附带免费模型或接入自有 OpenCode 兼容 provider

## 适用场景

- 在一体化的桌面环境里编写、编译并上传单片机代码
- 让 AI 帮忙创建、检查或修改嵌入式项目代码
- 通过串口日志和绘图观察传感器与运行时行为

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: ### Free, open-source AI coding workspace for microcontrollers.
> L32: |AI coding agent|Uses OpenCode to inspect the workspace, explain code, edit files, and help with embedded iteration

## 星数曲线

```mermaid
xychart-beta
    title "Razz19/Exort 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-23 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9a07ee4c6eca` · [字段定义](../../DATASET.md)*
