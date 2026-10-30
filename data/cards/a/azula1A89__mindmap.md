# azula1A89/mindmap

⭐ 20 · C++ · MIT · 推送 2025-12-12 · [GitHub](https://github.com/azula1A89/mindmap) · 个人维护

**C++ 编写的思维导图编辑器，可选接入本地 LLM 生成灵感**

基于 C++ 与 Dear ImGui 的桌面思维导图编辑器，提供手动/自动布局、自动布线、画布缩放平移、撤销重做、JSON 导入导出及 SVG/HTML 模板化导出。AI 功能为调用本地运行的 Ollama LLM 生成与上下文相关的节点想法，可修改提示词模板并右键选择模型；README 注明在支持 Structured Output 的模型（如 granite3.2、gemma 3）上效果最佳，小模型可能输出 schema 错误导致导入失败。Windows/Linux 提供预编译二进制，亦可经 MSYS2/CMake 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手动布局与自动布局/自动布线
- JSON 导入导出，模板引擎定制 SVG/HTML 导出
- 调用 Ollama LLM 生成上下文相关想法，可自定义提示词模板与选择模型
- Windows/Linux 提供预编译二进制

## 适用场景

- 绘制与整理思维导图，导出 SVG/HTML 分享
- 写作或头脑风暴时让本地 LLM 补充节点灵感
- 离线本地使用，数据以 JSON 文件保存

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L2: A simple yet fast mindmap editor written in C++. You can also call LLM to get some inspiration (if you run LLM local
> L14: * Call LLM to generate context related ideas.

## 星数曲线

```mermaid
xychart-beta
    title "azula1A89/mindmap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fd85a7731f61` · [字段定义](../../DATASET.md)*
