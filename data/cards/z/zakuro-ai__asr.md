# zakuro-ai/asr

⭐ 72 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/zakuro-ai/asr) · 组织维护

**PyTorch DeepSpeech2 英日语音识别训练框架**

基于 PyTorch 的 DeepSpeech2 语音识别实现，支持英语与日语，训练由 Sakura 1.0 运行时驱动：提供混合精度、异步评估与原子滚动检查点，全部行为由单一 YAML 配置控制。预训练日语模型在 JSUT 测试集达 CER=34，含 vanilla 同步参考循环与合成任务基准脚本。需 Python>=3.10 与 PyTorch，可用 pip 安装或从源码构建，Docker 镜像可经 make 命令生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DeepSpeech2（英/日）训练与评估，预训练日语模型 CER=34（JSUT）
- Sakura 运行时：混合精度、异步评估、异步检查点，单 YAML 驱动
- 贪心/束解码器、CTC 训练，断点自动续训
- time-to-performance 基准脚本与已提交结果

## 适用场景

- 训练或微调英/日 DeepSpeech2 语音识别模型
- 复现 Sakura 异步训练运行时的系统级基准
- 以 YAML 配置管理语音识别训练实验

## 场景标签

`语音识别` `模型训练` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L15: DeepSpeech2 speech recognition (English / Japanese) in PyTorch, trained with the
> L16: Sakura runtime. A clean, modular take on SeanNaren's

## 星数曲线

```mermaid
xychart-beta
    title "zakuro-ai/asr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 70 --> 73
    line [71, 72, 72]
```

2026-10-18 71 → 2026-10-28 72（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cea7dc3fed8a` · [字段定义](../../DATASET.md)*
