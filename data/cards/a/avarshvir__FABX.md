# avarshvir/FABX

⭐ 16 · Python · AGPL-3.0 · 推送 2026-07-11 · [GitHub](https://github.com/avarshvir/FABX) · [官网](https://jaiho-digital.onrender.com/products_pages/fabx.html) · 个人维护

**逆向工程与文件情报分析工具：解析复杂文件并用本地 LLM 解释**

面向逆向工程师、安全与 AI 研究者、学生的文件分析 Web 应用：上传可执行文件（.exe/.dll/.elf 等）、SQLite 数据库、ONNX/PyTorch/Pickle 机器学习模型或 JSON/YAML/INI/TOML 结构化文件，自动检测类型并路由到对应分析器，提取结构信息（函数、层、表、键等），生成 Plotly 交互式可视化图谱，再通过 Ollama 调用本地 LLM 解释结果、生成报告与推测性 C/C++ 重建。LLM 只接收压缩的结构化分析输出而非原始文件；Ollama 不可用时显示确定性回退说明。可执行文件的深度 Rizin 提取为预期引擎，当前快照仅完成检测与路由。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持可执行文件、SQLite、ONNX/PyTorch/Pickle 模型与 JSON/YAML/INI/TOML 五类文件分析
- LLM 只接收结构化分析输出，不直接读取原始文件，Ollama 缺失时回退到确定性说明
- 基于 NetworkX/Plotly 生成 ER 图、ONNX 计算图、参数图表等交互式可视化
- 提供 CLI 分析器，含 --unsafe-load 深度加载选项与 Pickle 安全警告

## 适用场景

- 分析陌生可执行文件或模型文件的结构并得到自然语言解释
- 检查 SQLite 数据库 schema、关系与样本数据并生成关系图
- 审计 ONNX/PyTorch/Pickle 模型的层结构与参数量，获取文档式报告

## 场景标签

`网络安全` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: FABX is an AI-powered reverse engineering and file intelligence tool. It is built to take complex files such as exec
> L137: FABX uses Ollama for local AI explanations. The LLM does not receive the raw uploaded file directly. Instead, FABX
> L78: FABX then builds model visualizations and asks Ollama to explain the model structure and, where reasonable, describ

## 星数曲线

```mermaid
xychart-beta
    title "avarshvir/FABX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2fbfbae53d62` · [字段定义](../../DATASET.md)*
