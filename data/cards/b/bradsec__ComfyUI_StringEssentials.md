# bradsec/ComfyUI_StringEssentials

⭐ 38 · Python · MIT · 推送 2026-07-03 · [GitHub](https://github.com/bradsec/ComfyUI_StringEssentials) · 个人维护

**ComfyUI 字符串处理自定义节点集，用于改写提示词与 LLM 输出文本**

面向 ComfyUI 用户的自定义节点包，提供 6 个字符串处理节点：文本框、按行列表移除字符串（String Strip）、多对搜索替换（String Multi Replace，支持正则与替换顺序）、条件追加（String Conditional Append）、多子串包含检查（String Contains Any，输出布尔值）与字符串预览。适用场景包括修改提示词或清洗 LLM 输出文本。无需额外 Python 依赖，可通过 ComfyUI Manager 安装或手动 git clone 到 custom_nodes 目录，兼容 V1 与 V3 双 API，在 ComfyUI 0.25.0 上验证。

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

- 6 个字符串节点：移除、多对替换、条件追加、包含检查、预览等
- 搜索替换支持正则模式与最长优先/输入顺序两种替换顺序
- 包含检查节点返回布尔值，可用于按提示词关键词加载 LoRA 的条件工作流
- 无需额外 Python 依赖，支持 V1/V3 双 API 入口

## 适用场景

- 清洗或改写 LLM 生成的提示词文本
- 在 ComfyUI 工作流中按提示词关键词做条件分支（如按需加载 LoRA）
- 确保提示词中必含特定关键词且不重复

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L1: # String Essentials - Custom nodes for ComfyUI
> L3: Simple string manipulation nodes for ComfyUI (strip/remove text strings, search and replace text strings, preview mo

## 星数曲线

```mermaid
xychart-beta
    title "bradsec/ComfyUI_StringEssentials 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6ef873dd08d6` · [字段定义](../../DATASET.md)*
