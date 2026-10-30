# liu-ziting/ThinkFlowAI

⭐ 172 · Vue · 推送 2026-02-06 · [GitHub](https://github.com/liu-ziting/ThinkFlowAI) · [官网](https://thinkflow-ai.lz-t.top) · 个人维护 · 中文 README

**输入一个想法，AI 扩展为可交互浏览的知识图谱的 Web 工作台**

基于 Vue 3 + Vite + @vue-flow 的 Web 应用：用户输入核心概念后由 AI 自动生成层次化的模块/子模块知识图谱，每个节点支持追问扩展、300-500 字深度回答（Markdown 渲染）、CogView/DALL-E 接口配图生成，以及全局拓扑扫描总结。数据与配置存于浏览器 IndexedDB/LocalStorage，支持自定义任意 OpenAI 兼容接口，默认演示接口经 Cloudflare Workers 转发至智谱 Bigmodel（glm-4-flash/cogview-3-flash）且有频率限制。提供在线演示站点，本地运行需 Node.js v18+，通过 git clone + npm install 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心想法→层次化知识图谱的 AI 发散生成
- 节点级追问扩展与 300-500 字深度回答（Markdown 渲染）
- CogView/DALL-E 接口为节点生成配图
- 本地优先存储（IndexedDB/LocalStorage），支持任意 OpenAI 兼容接口

## 适用场景

- 把模糊的想法快速展开为可浏览的知识结构
- 对图谱中任意分支继续追问并深挖专业详情
- 私有化部署并接入自己的 OpenAI 兼容模型接口

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L19: 在传统创作中，灵感往往是碎片化且模糊的。ThinkFlow AI 重新定义了这一过程：你只需输入一个核心想法，应用便会利用 AI 的发散性能力将其扩展为一套层次分明、可交互浏览的**知识图谱**。
> L38: - **专业级深度解析**：一键生成 300-500 字的深度回答，支持 Markdown 渲染，涵盖概念解释、案例分析与逻辑推演。

## 星数曲线

```mermaid
xychart-beta
    title "liu-ziting/ThinkFlowAI 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-30"]
    y-axis "stars" 171 --> 173
    line [172, 172]
```

2026-10-22 172 → 2026-10-30 172（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `783936cc738d` · [字段定义](../../DATASET.md)*
