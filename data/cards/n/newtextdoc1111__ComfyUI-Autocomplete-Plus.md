# newtextdoc1111/ComfyUI-Autocomplete-Plus

⭐ 194 · JavaScript · MIT · 推送 2026-02-21 · [GitHub](https://github.com/newtextdoc1111/ComfyUI-Autocomplete-Plus) · 个人维护

**ComfyUI 提示词输入辅助节点：标签自动补全与相关标签显示**

面向 ComfyUI 用户的自定义节点，为任意文本输入框提供输入辅助：基于 Danbooru/e621 标签的实时自动补全（按帖子数降序、含中日韩别名）、基于共现数据的相关标签列表、失去焦点时自动格式化提示词文本，并支持用户自定义 CSV。标签数据 CSV 托管在 HuggingFace，首次启动自动下载；e621 需手动放置 CSV 且不支持相关标签。可通过 ComfyUI-Manager 或手动克隆到 custom_nodes 安装。

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

- Danbooru/e621 标签实时自动补全，含日文假名与中日韩别名搜索
- 基于共现 CSV 的相关标签显示
- 提示词自动格式化（清理逗号空格、可配置触发方式）
- 支持用户自定义 CSV 与批量标签插入（伪 Chants）

## 适用场景

- 在 ComfyUI 编写提示词时快速查找 Danbooru 标签
- 通过相关标签扩展提示词描述
- 用自定义 CSV 补全常用 meta 标签与固定标签组合

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: **ComfyUI-Autocomplete-Plus** is a custom node that provides multiple input assistance features for any text area in
> L14: - **:mag:Autocomplete**: Displays tag suggestions in real-time based on your input as you type.

## 星数曲线

```mermaid
xychart-beta
    title "newtextdoc1111/ComfyUI-Autocomplete-Plus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 193 --> 195
    line [194, 194]
```

2026-10-18 194 → 2026-10-27 194（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e46a1d45a89c` · [字段定义](../../DATASET.md)*
