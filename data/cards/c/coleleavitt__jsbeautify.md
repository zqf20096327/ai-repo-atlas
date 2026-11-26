# coleleavitt/jsbeautify

⭐ 11 · Rust · MIT · 推送 2026-11-24 · [GitHub](https://github.com/coleleavitt/jsbeautify) · 个人维护

**给 AI agent 用的 Rust JS 反混淆器**

基于 Oxc 的 Rust CLI 反混淆器：把压缩/打包/混淆的 JavaScript 转为可读且行为等价的代码。输出与日志按模型可读设计（JSON/DOT/阶段日志），scope/cfg/split-sources 命令支持 agent 不加载整个 bundle 即可查询。支持 webpack、Turbopack、esbuild、Bun、Angular、javascript-obfuscator、Akamai 等检测；--project 跨 chunk 统一命名；两次重解析检查点保证不输出非法 JS；附带 refinement loop 文档让 agent 自主修复本工具的缺陷。需 Rust 1.97+，经 cargo 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- --project 对整个 code-split build 的跨文件绑定统一命名
- 输出/日志为模型可查询格式（JSON、DOT、阶段日志）
- 两处检查点重解析，非法 JavaScript 不报成功
- 仓库内含 AGENTS.md/CLAUDE.md 与 refinement loop 供 agent 改进工具自身

## 适用场景

- 恶意软件分析中还原混淆 JS 为可读代码
- 让 Claude Code/Codex 等 agent 分析大型打包产物
- 还原 webpack/esbuild 等打包器产物的原始命名

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3:  The JavaScript deobfuscator built for AI agents, and refined by them.
> L19: These days agents, not people, read most deobfuscated code. jsbeautify is
> L112: 3. **Autonomous refinement.** Agents improve the tool they rely on. The repo


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8029f852d60c` · [字段定义](../../DATASET.md)*
