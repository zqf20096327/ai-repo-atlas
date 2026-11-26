# tony3liu/eido

⭐ 308 · Rust · GPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/tony3liu/eido) · [官网](https://cairno.cn/eido/) · 个人维护 · 中文 README

**面向 macOS 用户的 AI 工作区：会话为中心完成任务**

基于 Zed 编辑器与 pi agent 构建的本地 macOS 应用，将任务、对话与结果文件保持在同一工作区。提供原生代码编辑与变更审查、Browser Use 与 Computer Use（捆绑 Chromium 与桌面驱动）、全局 Agent 权限控制（Ask Before Actions/Full Access）、自定义 API 接入、图像生成扩展与实验性研究文档提取功能。当前版本 0.0.5，仅支持 Apple Silicon 且标注为早期发布，未通过 Apple 公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置任务/文件/分屏视图，会话与原生编辑审查结合
- Browser Use 与 Computer Use，捆绑 Chromium 与桌面驱动
- 全局 Agent 访问控制（Ask Before Actions / Full Access）
- 自定义 API 连接与图像生成（gpt-image-1 系列模型 ID）

## 适用场景

- 在对话中完成代码修改并逐项审查接受变更
- 让 AI 操作浏览器与桌面应用完成网站流程
- 基于本地文档与外部来源做研究对比并保留证据

## 场景标签

`GUI 自动化` `编码 Agent` `代码审查` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L17: Eido is a native AI workspace built on Zed and the official, unmodified pi agent. Start with an outcome, bring in r
> L40: Reference relevant files with `@`, attach supporting material, and continue earlier tasks with their saved context.
> L66: 3. **Set Agent Access.** Start with **Ask Before Actions**, or choose **Full Access** to let pi decide how to use e

## 星数曲线

```mermaid
xychart-beta
    title "tony3liu/eido 星数(近 17 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-18", "2026-11-20", "2026-11-26"]
    y-axis "stars" 112 --> 325
    line [129, 136, 145, 153, 165, 176, 186, 193, 203, 211, 136, 284, 303, 306, 307, 308, 308]
```

2026-10-24 129 → 2026-11-26 308（+179）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `68c8567375af` · [字段定义](../../DATASET.md)*
