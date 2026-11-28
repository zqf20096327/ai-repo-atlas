# AbrahamPaulJ/tensorlens

⭐ 4 · C++ · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/AbrahamPaulJ/tensorlens) · 个人维护

**IDA 插件：在二进制中定位嵌入的 ML 模型并还原 TFLite 内核**

面向逆向工程师的 IDA 插件，处理二进制中的两类目标：嵌入的模型（TFLite flatbuffer、ONNX protobuf、ncnn、ExecuTorch，含 gzip/tar 内嵌与 APK 携带场景）和被 strip 的 TFLite 运行时（通过解码 op resolver 命名内核的 Init/Free/Prepare/Eval 并应用 TFLite C 类型）。提供图视图、内核与模型节点的互链、HTML/JSON 报告，以及脱离 IDA 的命令行扫描器 tensorlens-scan。无 Python、无外部依赖，支持 IDA Free 9.5。README 声明目前不解析 GGUF 格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定位并结构化校验嵌入的 TFLite/ONNX/ncnn/ExecuTorch 模型（含 gzip/tar/APK 内嵌）
- 从 op resolver 还原 stripped 二进制中 TFLite 内核命名与类型，无需符号
- 模型图以 IDA 图呈现，操作符与执行内核双向跳转
- 独立命令行扫描器可处理文件、APK、AAR、wheel

## 适用场景

- 安全审查 App 内置的 AI 模型及其处理输入的原生代码
- 提取模型导出为 .tflite/.onnx 供进一步查看
- 对 stripped 的 TFLite 运行时做分类与漏洞研究

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **ML models and the runtimes that run them, inside the binary, in IDA.**
> L20: |**Find models**|TFLite, ONNX, ncnn and ExecuTorch, embedded anywhere in the database or the input file, also insid
> L170: No Python, no dependencies: the flatbuffer, protobuf and zip readers are built in. Works in every IDA


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `b279613d84a4` · [字段定义](../../DATASET.md)*
