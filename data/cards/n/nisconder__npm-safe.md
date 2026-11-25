# nisconder/npm-safe

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/nisconder/npm-safe) · [官网](https://www.npmjs.com/package/@npm-safe/core) · 组织维护 · 中文 README

**npm 供应链安全扫描器：装前检查包风险，支持 CLI/CI/桌面**

本地优先的 npm 供应链扫描工具：默认读取发布元数据与 README 信号，可选 deep scan 在内存中校验并解析 tarball，检测安装脚本、混淆、typosquatting、可执行内容、进程/网络组合等，输出可解释的 0–100 安全分。10 条元数据规则 + 17 条内容规则，支持本地插件扩展。LLM 语义分析与 source review 均默认关闭，需 API key；模型结果不能清除静态告警或抬高静态分。提供 CLI、安装门控、CI 退出码、SQLite 历史库及打包为 ZIP 的 Neutralinojs 桌面应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认静态分析全部本地运行，无账号、无托管后端
- deep scan 在严格字节预算内解析 tarball，不落盘不执行
- 可选 LLM source review 要求模型引用原文并给出 UTF-16 偏移
- 安装门控低于阈值（默认 85）需手动确认，CI 以退出码阻断构建

## 适用场景

- 安装陌生 npm 包之前先检查其供应链风险信号
- 在 CI 流水线中扫描 lockfile 依赖并对高危项使构建失败
- 比较某个包两个发布版本之间新增/消失的风险证据
- 为 Codex、Claude Code、Gemini CLI 等 agent 安装安全技能

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: `npm-safe` checks published metadata and README signals by default; an opt-in
> L116: API key, static analysis continues normally. Providers: OpenAI, Gemini,
> L176: `npm-safe ci` scans a project's dependencies and fails the build when any


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `e1f208c7bd64` · [字段定义](../../DATASET.md)*
