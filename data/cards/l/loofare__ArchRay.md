# loofare/ArchRay

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/loofare/ArchRay) · [官网](https://archray.dev) · 个人维护 · 中文 README

**给 AI 编码代理生成离线 3D/2D 架构图的开发工具**

ArchRay 以技能/命令形式装入 Claude Code、Cursor、Codex、Pi、Antigravity 等 AI 编码代理，由代理读取源码做语义抽取，再用确定性 ELK 布局生成 100% 离线的单文件 HTML 架构图，支持 L0–L9 分层切片、健康热点、可替换性分析与迁移提示复制。所有节点带 sourcePaths 出处，区分实测与估算指标。运行需 Node.js 20+ 与 curl/tar；通过 shell 安装脚本部署，另提供 doctor/validate/build/update/uninstall 等 CLI 维护命令。

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

- AI 代理语义抽取 + 确定性 ELK 布局的两段式管线
- 生成零网络单文件 HTML，含 167 个内嵌技术 logo、PNG 导出与离线二维码
- 每个节点与依赖引用 sourcePaths，区分 measured 与 ≈ 估算指标
- 支持 L0–L9 层切片、主题切换与中英文别名

## 适用场景

- 让 AI 编码代理分析仓库并生成可交互架构图
- 识别代码库耦合热点与供应商锁定风险
- 离线环境下向团队交付带源码出处的架构视图

## 场景标签

 · 领域:开发者工具/架构可视化

## 证据(README 行号)

> L5:  Equip your AI coding agent to read real source code and build interactive, 100% offline 3D Spatial &amp; 2D Bento a
> L44:  AI Coding Agent (/archray) -> Deterministic ELK -> Offline Single HTML" width="100%" />


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e067b0d50b4f` · [字段定义](../../DATASET.md)*
