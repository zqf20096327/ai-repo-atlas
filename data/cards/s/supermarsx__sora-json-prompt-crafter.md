# supermarsx/sora-json-prompt-crafter

⭐ 49 · TypeScript · MIT · 推送 2026-09-18 · [GitHub](https://github.com/supermarsx/sora-json-prompt-crafter) · [官网](https://sora-json-prompt-crafter.lovable.app) · 个人维护

**浏览器端 Sora 视频 JSON 提示词构建工具，本地生成不留痕**

基于 Vite/React/TypeScript 的 Web 界面，通过滑块与下拉框调整风格预设、宽高比、时长、摄像机与运动等参数，实时生成可复制到 Sora 生成模型的 JSON 提示词片段，支持负向提示词编辑与差异高亮。数据仅存本地浏览器，支持最多 100 条历史、导入导出、自定义 CSS/JS 注入与 20 余种语言。另提供 npm CLI（sora-crafter）与 Docker 构建方式，需 Node.js 22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 滑块/下拉式参数调整并实时生成 JSON，含差异高亮
- 提示词数据仅存本地浏览器，不做提示词追踪
- 历史面板保存最多 100 条 JSON，支持导入导出
- 提供 CLI（npx ts-node / sora-crafter）与 Docker 两种非浏览器用法

## 适用场景

- 为 Sora 视频生成模型手工调参并产出 JSON 提示词
- 离线或本地保存/管理常用提示词组合
- 通过 CLI 批量生成提示词 JSON 文件

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L17: Sora JSON Prompt Crafter is a web interface for building specially crafted prompts for Sora's
> L19: aspect ratio, video duration and more. The app generates a JSON snippet you can copy and

## 星数曲线

```mermaid
xychart-beta
    title "supermarsx/sora-json-prompt-crafter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dd89f7c21bb2` · [字段定义](../../DATASET.md)*
