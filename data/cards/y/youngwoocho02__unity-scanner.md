# youngwoocho02/unity-scanner

⭐ 27 · Go · MIT · 推送 2026-05-14 · [GitHub](https://github.com/youngwoocho02/unity-scanner) · 个人维护

**为 AI agent 压缩 Unity 资产输出的 CLI 扫描工具**

面向 AI agent 工作流的 Unity 项目资产扫描 CLI，提供 list/read/search/refs 四个命令，直接读取当前项目文件，无需缓存或 Unity Editor 连接。它将 Unity YAML 对象转为 GameObject 树、折叠重复组件集合与编号名称、把 GUID 解析为路径、省略 .meta 文件，从而把 CLI 输出压缩后再交给模型，README 示例中字符量减少约 80%-99%。支持文件级并行扫描与 --depth/--limit 等控制选项，通过安装脚本分发二进制，源码用 Go 构建。

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

- list/read/search/refs 四命令覆盖资产列举、YAML 结构化读取、搜索与 GUID 引用查找
- Unity 感知压缩：层级树、组件组折叠、GUID 解析为路径、.meta 省略
- 无缓存、无需 Editor 连接，直接读取当前项目文件
- 广域搜索按文件并行，示例中名称搜索 1500ms 降至 600ms

## 适用场景

- 让 AI agent 以更少 token 浏览和理解 Unity 项目资产
- 查找某资产或 GUID 被哪些 prefab/scene/asset 引用
- 先以压缩视图定位目标，再下钻查看组件字段细节

## 场景标签

 · 领域:游戏开发/开发者工具

## 证据(README 行号)

> L22: 1. Reduce token cost. Like RTK, reduce CLI output before it reaches the model by compressing repeated Unity paths, 
> L28: - CLI reads current files only: no cache, no required editor state.

## 星数曲线

```mermaid
xychart-beta
    title "youngwoocho02/unity-scanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5733c6f7604a` · [字段定义](../../DATASET.md)*
