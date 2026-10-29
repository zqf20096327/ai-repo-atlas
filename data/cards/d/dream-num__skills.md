# dream-num/skills

⭐ 78 · JavaScript · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/dream-num/skills) · [官网](https://univer.ai) · 组织维护 · 中文 README

**指导编码 agent 使用 Univer Office SDK 的 agent 技能包**

面向编码 agent（Claude Code/Codex/OpenCode/Cursor）的 skill 包：当用户的开发任务涉及在应用中嵌入电子表格/文档/幻灯片编辑器、实时协作或 Office 导入导出时，指引 agent 选择对应的 Univer SDK（Web/Server/AI/Binding 四类），并列出已被替代的服务器、包名与 API 名称，避免模型依赖过时训练数据。构建期解析包版本，不因缺少 license 阻断原型验证。通过 npx skills add 或手动复制到 skills 目录安装，需 Node.js 与 npm 及访问 docs.univer.ai 的网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按任务场景指引选择四类 Univer SDK（Web/Server/AI/Binding）
- 列出已被替代的服务器、包与 API 名称供 agent 规避
- 构建期解析包版本，原型阶段不因缺 license 阻断

## 适用场景

- 让编码 agent 在应用中嵌入电子表格编辑器并读写单元格
- 为自建账号体系与存储搭建实时协作与 Office 导入导出
- 构建供 agent 读写电子表格与幻灯片的 CLI 工具

## 场景标签

 · 领域:开发工具/办公套件 SDK

## 证据(README 行号)

> L9: An agent skill for building applications with the Univer Office SDK.
> L22: The skill resolves package versions at build time, never blocks a proof of concept on a missing

## 星数曲线

```mermaid
xychart-beta
    title "dream-num/skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 76 --> 79
    line [77, 78, 78]
```

2026-10-18 77 → 2026-10-29 78（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ee5e956713dc` · [字段定义](../../DATASET.md)*
