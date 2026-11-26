# AryabhattaLabs/agent-tool-result-reducer

⭐ 4 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/AryabhattaLabs/agent-tool-result-reducer) · [官网](https://aryabhattalabs.com/#developers) · 组织维护

**为 LLM agent 压缩超大 JSON 工具结果并保留缺失说明的 Python 库**

零依赖 Python 库，插入在「工具返回结果」与「写入模型上下文」之间：按字符预算选取字段、跨条目丢弃最宽字段、只在整条目边界裁剪，保证输出始终为合法 JSON；所有被省略的内容通过 `_meta` 块显式告知模型，附条目计数、来源总数与被丢字段。核心函数 `reduce_tool_result` 提供 select 投影、自动适配、单大对象的 outline 降级与非 JSON 文本的字符截断回退。面向 agent 构建者，OpenAI/Anthropic/LangChain 示例各只需一行改动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按字符预算的确定性压缩，输出始终为合法 JSON 且只在整条目边界裁剪
- 通过 `_meta` 块显式告知模型收到与未收到什么，防止部分结果被当作完整结果
- select 投影支持点路径字段选择，含拼写错误与信封前缀的防护与自动修复
- 零运行时依赖，标准库实现

## 适用场景

- agent 循环中搜索/API 类工具返回超大结果，需要塞进上下文预算
- 防止模型把被截断的部分结果误报为完整结果
- 在工具 schema 中让模型按需选择字段以节省每轮 token

## 场景标签

 · 领域:LLM 基础设施/agent 工具链

## 证据(README 行号)

> L12: A zero-dependency Python library that fits an API/tool response into a
> L53: Give agent builders a drop-in function that sits between **"tool returned


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `433f07f7d175` · [字段定义](../../DATASET.md)*
